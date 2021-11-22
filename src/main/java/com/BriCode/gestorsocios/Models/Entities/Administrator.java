package com.BriCode.gestorsocios.Models.Entities;

import lombok.*;
import org.hibernate.Hibernate;

import javax.persistence.*;
import java.util.Objects;

@Entity
@Getter
@Setter
@ToString
@RequiredArgsConstructor
public class Administrator {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "idadmin", columnDefinition = "INT(10) UNSIGNED")
    public Integer idadmin;
    @Column(name = "usernae", columnDefinition = "VARCHAR")
    public String username;
    @Column(name = "password", columnDefinition = "VARCHAR")
    public String password;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || Hibernate.getClass(this) != Hibernate.getClass(o)) return false;
        Administrator that = (Administrator) o;
        return idadmin != null && Objects.equals(idadmin, that.idadmin);
    }

    @Override
    public int hashCode() {
        return getClass().hashCode();
    }
}
