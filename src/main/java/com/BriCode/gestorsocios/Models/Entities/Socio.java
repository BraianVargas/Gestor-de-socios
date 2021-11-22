package com.BriCode.gestorsocios.Models.Entities;


import lombok.*;
import org.hibernate.Hibernate;

import javax.persistence.*;
import java.util.Objects;

@Entity
@RequiredArgsConstructor
@Getter
@Setter
@ToString
public class Socio {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "idsocio", columnDefinition = "INT(10) UNSIGNED")
    public Integer idsocio;
    @Column(name = "nombre", columnDefinition = "VARCHAR")
    public String nombre;
    @Column(name = "apellido", columnDefinition = "VARCHAR")
    public String apellido;
    @Column(name = "dni", columnDefinition = "VARCHAR")
    public String dni;
    @Column(name = "pago")
    public Boolean pago;
    @Column(name = "mediodepago")
    public String mediodepago;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || Hibernate.getClass(this) != Hibernate.getClass(o)) return false;
        Socio socio = (Socio) o;
        return idsocio != null && Objects.equals(idsocio, socio.idsocio);
    }

    @Override
    public int hashCode() {
        return getClass().hashCode();
    }
}
