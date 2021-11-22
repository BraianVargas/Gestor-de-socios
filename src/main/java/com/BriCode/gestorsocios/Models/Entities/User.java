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
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "iduser", columnDefinition = "INT(10) UNSIGNED")
    public Integer iduser;
    @Column(name = "nombre", columnDefinition = "VARCHAR")
    public String nombre;
    @Column(name = "apellido", columnDefinition = "VARCHAR")
    public String apellido;
    @Column(name = "dni", columnDefinition = "VARCHAR")
    public String dni;
    @Column(name = "direccion", columnDefinition = "VARCHAR")
    public String direccion;
    @Column(name = "telefono", columnDefinition = "VARCHAR")
    public String telefono;
    @Column(name = "mail", columnDefinition = "VARCHAR")
    public String mail;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || Hibernate.getClass(this) != Hibernate.getClass(o)) return false;
        User user = (User) o;
        return iduser != null && Objects.equals(iduser, user.iduser);
    }

    @Override
    public int hashCode() {
        return getClass().hashCode();
    }
}
