package io.github.systemgatherer.web;

import com.codahale.metrics.annotation.Timed;
import io.github.systemgatherer.configuration.Plugin;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.util.List;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class Root {
    private final List<Plugin> plugins;

    public Root(List<Plugin> plugins) {
        this.plugins = plugins;
    }

    @GET
    @Timed
    public List<Plugin> root() {
        return plugins;
    }
}
