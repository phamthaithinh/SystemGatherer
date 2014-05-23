package io.github.systemgatherer.plugins.impl;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.github.systemgatherer.configuration.Plugin;
import io.github.systemgatherer.plugins.IExecutor;
import io.github.systemgatherer.response.Response;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Date;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
public class Executor implements IExecutor {

    @Override
    public Response runScript(Plugin plugin) {

        String arguments = plugin.getPath() + " " + plugin.getArguments()[0]
                + " " + plugin.getArguments()[1];

        if (plugin.getArguments().length > 2) {
            arguments = arguments + " " + plugin.getArguments()[2];
        }

        String[] cmd = {
                "/bin/bash",
                "-c",
                "echo output | " + arguments
        };

        String result = "";
        int code = 0;
        try {
            String line;
            Process p = Runtime.getRuntime().exec(cmd);
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while ((line = input.readLine()) != null) {
                result = result + line;
            }
            input.close();
            code = p.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
        return buildResponse(toJsonObject(result), code);
    }

    private Response buildResponse(Object info, int code) {
        return new Response(code, new Date(), info);
    }

    private Object toJsonObject(String info) {
        ObjectMapper objectMapper = new ObjectMapper();
        JsonNode rootNode = null;
        try {
            rootNode = objectMapper.readTree(info);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return rootNode;
    }
}
