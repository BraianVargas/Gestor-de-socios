package com.BriCode.gestorsocios.Models.Dtos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


@AllArgsConstructor
@NoArgsConstructor
@Data
public class SocioDto {
    public Integer idsocio;
    public String nombre;
    public String apellido;
    public String dni;
    public Boolean pago;
    public String mediodepago;
}
