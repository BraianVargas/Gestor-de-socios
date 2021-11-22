package com.BriCode.gestorsocios.Models.Repositories;

import com.BriCode.gestorsocios.Models.Entities.Administrator;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository("administratorRepository")
public interface AdministratorRepository extends JpaRepository<Administrator, Integer> {
}
