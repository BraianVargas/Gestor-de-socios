package com.BriCode.gestorsocios.Models.Dtos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Data
public class AdministratorDto {
    public Integer idadmin;
    public String username;
    public String password;
}
