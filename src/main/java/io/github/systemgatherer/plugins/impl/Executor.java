package io.github.systemgatherer.plugins.impl;

import io.github.systemgatherer.configuration.Plugin;
import io.github.systemgatherer.plugins.IExecutor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
public class Executor implements IExecutor {

    @Override
    public String runScript(Plugin plugin) {

        String arguments = plugin.getPath() + " " + plugin.getArguments()[0]
                + " " + plugin.getArguments()[1];

        if (plugin.getArguments().length > 2) {
            arguments = arguments + " " + plugin.getArguments()[2];
        }

        String[] cmd = {
                "/bin/bash",
                "-c",
                "echo password | python3 " + arguments
        };

        String result = "";
        try {
            String line;
            Process p = Runtime.getRuntime().exec(cmd);
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while ((line = input.readLine()) != null) {
                result = result + line;
            }
            input.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return result;
    }
}
