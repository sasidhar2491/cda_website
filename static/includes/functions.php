<?php

if(!function_exists("redirect_url")) {

		function redirect_url($page){

			header("location: ".$page);

			exit;

		}

	}
	
	 function text_data( $id ) {

	  global $obj_db;

	  $total=$obj_db->fetchRow("select * from editpages where edit_id=".(int)$id."");

	  return $total['page_content'];

  }
?>