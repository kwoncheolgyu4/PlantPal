package com.future.plant.member.dao;

import org.apache.ibatis.annotations.Mapper;

import com.future.plant.member.vo.MemberVO;

@Mapper
public interface IMemberDAO {
	
	public int signUpMember(MemberVO vo);
	
	public MemberVO loginMember(MemberVO vo);
	
}
