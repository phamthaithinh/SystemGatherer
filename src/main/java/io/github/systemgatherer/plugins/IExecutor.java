package io.github.systemgatherer.plugins;

import io.github.systemgatherer.configuration.Plugin;
import io.github.systemgatherer.response.Response;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
public interface IExecutor {

    Response runScript(Plugin plugin);
}
