package com.BriCode.gestorsocios.Models.Mappers;

import com.BriCode.gestorsocios.Models.Dtos.AdministratorDto;
import com.BriCode.gestorsocios.Models.Entities.Administrator;
import org.springframework.stereotype.Component;

import java.util.Optional;

@Component
public class AdministratorMapper {
    public AdministratorDto entityToDto(Administrator entity){
        return Optional
                .ofNullable(entity)
                .map(
                        ent -> new AdministratorDto(
                                ent.getIdadmin(),
                                ent.getUsername(),
                                ent.getPassword()
                        )
                )
                .orElse(new AdministratorDto());
    }
    public Administrator dtoToEntity(AdministratorDto dto){
        Administrator entity = new Administrator();
        entity.setIdadmin(dto.getIdadmin());
        entity.setUsername(dto.getUsername());
        entity.setPassword(dto.getPassword());
        return entity;
    }
}
