package io.github.systemgatherer;

import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;
import io.github.systemgatherer.configuration.SGConfiguration;
import io.github.systemgatherer.web.Root;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
public class SystemGatherer extends Application<SGConfiguration> {
    @Override
    public void initialize(Bootstrap<SGConfiguration> bootstrap) {

    }

    @Override
    public void run(SGConfiguration configuration, Environment environment) throws Exception {
        final Root root = new Root(configuration.getPlugins());

        environment.jersey().register(root);
    }

    public static void main(String[] args) throws Exception {
        new SystemGatherer().run(args);
    }
}