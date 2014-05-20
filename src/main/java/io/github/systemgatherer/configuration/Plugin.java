package io.github.systemgatherer.configuration;

import lombok.Data;
import org.hibernate.validator.constraints.NotEmpty;

import java.util.List;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
@Data
public class Plugin {
    @NotEmpty
    private String name;
    @NotEmpty
    private String path;
    @NotEmpty
    private List<String> arguments;

    public Plugin() {
    }

    public Plugin(String name, String path, List<String> arguments) {
        this.name = name;
        this.path = path;
        this.arguments = arguments;
    }
}
