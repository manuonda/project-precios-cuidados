package com.dgarcia.preciocuidados;

import org.springframework.boot.SpringApplication;

public class TestBackPrecioCuidadosApplication {

	public static void main(String[] args) {
		SpringApplication.from(BackPrecioCuidadosApplication::main).with(TestcontainersConfiguration.class).run(args);
	}

}
