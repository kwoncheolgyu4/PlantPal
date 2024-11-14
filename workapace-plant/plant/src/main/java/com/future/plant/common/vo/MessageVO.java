package com.future.plant.common.vo;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class MessageVO {
	
	private boolean result;
	private String title;
	private String message;
	private String url;
	private String urlTitle;
	
	public MessageVO() {
	}

	public MessageVO(boolean result, String title, String message, String url, String urlTitle) {
		super();
		this.result = result;
		this.title = title;
		this.message = message;
		this.url = url;
		this.urlTitle = urlTitle;
	}

}
