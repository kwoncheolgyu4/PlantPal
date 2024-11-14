package com.future.plant.member.vo;

import com.future.plant.common.valid.Login;
import com.future.plant.common.valid.Regist;

import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;
import lombok.Data;

@Data
public class MemberVO {
	
	@NotEmpty(message="아이디 필수!!", groups={Login.class, Regist.class})
	String memId;
	// \\w -> [a~zA~Z0~9]
	@Pattern(regexp="^[a-zA-Z0-9]{4,10}$", message="패스워드는 영문 숫자 4 ~ 10로 입력!", groups={Login.class, Regist.class})
	String memPw;
	@Size(min=1, max=20, message="이름은 20자 이내로 입력!!", groups={Regist.class})
	String memNm;
	
	
}
