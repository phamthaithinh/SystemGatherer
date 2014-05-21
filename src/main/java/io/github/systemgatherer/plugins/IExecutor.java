package io.github.systemgatherer.plugins;

import io.github.systemgatherer.configuration.Plugin;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
public interface IExecutor {

    String runScript(Plugin plugin);
}
