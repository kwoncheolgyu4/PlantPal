package com.future.plant.common.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {
	
	@Bean
	SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
	        http
		        .cors(cors -> cors.disable()) // CORS 방지
		        .csrf(csrf -> csrf.disable()) // CSRF 방지
		        .formLogin(formLogin -> formLogin.disable()) // 기본 로그인 창 비활성화
		        .headers(headers -> headers.frameOptions(frameOptions -> frameOptions.disable())); // 프레임 옵션 비활성화

	
	    return http.build();
	}
	
	@Bean
    PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
