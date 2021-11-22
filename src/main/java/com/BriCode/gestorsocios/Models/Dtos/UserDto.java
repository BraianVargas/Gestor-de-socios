package com.BriCode.gestorsocios.Models.Dtos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
public class UserDto {
    public Integer iduser;
    public String nombre;
    public String apellido;
    public String dni;
    public String direccion;
    public String telefono;
    public String mail;
}
