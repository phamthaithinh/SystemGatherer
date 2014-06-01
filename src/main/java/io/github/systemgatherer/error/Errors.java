package io.github.systemgatherer.error;

import lombok.Getter;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */

@Getter
public enum Errors {
    NOT_EXECUTABLE(100, "Script file not executable"),
    NOT_EXIST(101, "Script file not exist");

    private int code;
    private String desc;

    Errors(int code, String desc) {
        this.code = code;
        this.desc = desc;
    }
}
