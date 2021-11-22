package com.BriCode.gestorsocios.Models.Mappers;

import com.BriCode.gestorsocios.Models.Dtos.UserDto;
import com.BriCode.gestorsocios.Models.Entities.User;
import org.springframework.stereotype.Component;

import java.util.Optional;

@Component
public class UserMapper {
    public UserDto entityToDto(User entity){
        return Optional
                .ofNullable(entity)
                .map(
                        ent -> new UserDto(
                                ent.getIduser(),
                                ent.getNombre(),
                                ent.getApellido(),
                                ent.getDni(),
                                ent.getDireccion(),
                                ent.getTelefono(),
                                ent.getMail()
                        )
                )
                .orElse(new UserDto());
    }
    public User dtoToEntity(UserDto dto){
        User entity = new User();
        entity.setIduser(dto.getIduser());
        entity.setNombre(dto.getNombre());
        entity.setApellido(dto.getApellido());
        entity.setDni(dto.getDni());
        entity.setDireccion(dto.getDireccion());
        entity.setTelefono(dto.getTelefono());
        entity.setMail(dto.getMail());
        return  entity;
    }
}
