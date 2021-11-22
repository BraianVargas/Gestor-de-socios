package com.BriCode.gestorsocios.Models.Mappers;

import com.BriCode.gestorsocios.Models.Dtos.SocioDto;
import com.BriCode.gestorsocios.Models.Entities.Socio;
import org.springframework.stereotype.Component;

import java.util.Optional;

@Component
public class SocioMapper {
    public SocioDto entityToDto(Socio entity){
        return Optional
                .ofNullable(entity)
                .map(
                        ent -> new SocioDto(
                                ent.getIdsocio(),
                                ent.getNombre(),
                                ent.getApellido(),
                                ent.getDni(),
                                ent.getPago(),
                                ent.getMediodepago()
                        )
                )
                .orElse(new SocioDto());
    }
    public Socio socioDtoToEntity(SocioDto dto){
        Socio entity = new Socio();
        entity.setIdsocio(dto.getIdsocio());
        entity.setNombre(dto.getNombre());
        entity.setApellido(dto.getApellido());
        entity.setDni(dto.getDni());
        entity.setPago(dto.getPago());
        entity.setMediodepago(dto.getMediodepago());
        return entity;
    }

}
