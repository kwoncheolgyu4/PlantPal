package com.future.plant.plantmap.web;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class PlantMapController {
	
	
	@GetMapping("/plantmap")
	public String plantMap() {
		return "map/plantMap";
	}
	
}
