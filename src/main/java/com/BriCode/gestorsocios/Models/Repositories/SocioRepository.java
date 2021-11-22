package com.BriCode.gestorsocios.Models.Repositories;

import com.BriCode.gestorsocios.Models.Entities.Socio;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository("socioRepository")
public interface SocioRepository extends JpaRepository<Socio, Integer> {
}
