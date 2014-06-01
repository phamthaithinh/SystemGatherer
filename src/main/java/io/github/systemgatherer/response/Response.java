package io.github.systemgatherer.response;

import lombok.Data;

import java.util.Date;

/**
 * @author Rinat Muhamedgaliev aka rmuhamedgaliev
 */
@Data
public class Response {
    private final int code;
    private final Date date;
    private final Object info;
    private final String name;

    public Response(int code, Date date, Object info, String name) {
        this.code = code;
        this.date = date;
        this.info = info;
        this.name = name;
    }
}
