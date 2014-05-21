package io.github.systemgatherer.web;

import com.codahale.metrics.annotation.Timed;
import io.github.systemgatherer.configuration.Plugin;
import io.github.systemgatherer.plugins.IExecutor;
import io.github.systemgatherer.plugins.impl.Executor;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class Root {
    private final List<Plugin> plugins;
    private Map<String, Plugin> pluginMap = new HashMap<>();

    private final IExecutor executor = new Executor();

    public Root(List<Plugin> plugins) {
        this.plugins = plugins;

        for (Plugin plugin: plugins) {
            pluginMap.put(plugin.getName(), plugin);
        }
    }

    @GET
    @Timed
    public String root(@QueryParam("name") String name) {
        return executor.runScript(pluginMap.get(name));
    }
}
