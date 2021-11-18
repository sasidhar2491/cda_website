<?php



error_reporting(0);



if(!class_exists("db")) {



	class db 



	{  



		 //Mysql connection start



		 public function open_connection()



		 {



				if($_SERVER['HTTP_HOST']=='localhost') {



					$hostname = "localhost";



					$username = "root";



					$password = "";



					$database = "heaven1";



				} else {


                     //hostgator 
					//$hostname = "localhost";
					//$username = "wwwheave_wall";
					//$password = "wall@123";
					//$database = "wwwheave_wall";
					
					$hostname = "HeavensWall.db.13955726.hostedresource.com";

					$username = "HeavensWall";

					$password = "Heavens@425";

					$database = "HeavensWall";



				}



					



					$connect = mysql_connect($hostname,$username,$password);



					$select_db = mysql_select_db($database);



		 }



		 //Mysql connection close



		 public function close_connection()



		 {



				mysql_close();



		 }



		 



		//Multiple rows fetching



		function fetchArray($query_result){		



			$array = mysql_fetch_array($query_result,MYSQL_ASSOC);



			return $array;



		}



		



		//Get query result



		function get_qresult($get_query){



			$get_result = mysql_query($get_query)or die($get_query.mysql_query());



			return $get_result;



		}



		



		//getting single record



		function fetchRow($select_query){



			$select_result=mysql_query($select_query)or die($select_query.mysql_query());



			$select_row = mysql_fetch_array($select_result);



			return $select_row;



		}	



		



		//getting selected field in a record



		function fetch_field($select_query){



			$select_result=mysql_query($select_query);



			$select_row = mysql_fetch_array($select_result);



			if($select_row) return $select_row[0]; else return 0;



		}	



			



		//count records



		function fetchNum($select_query){



			$select_result=mysql_query($select_query) or die(mysql_error());



			$get_num = mysql_num_rows($select_result);



			return $get_num;



		}



	} 



}





$baseurl="http://www.heavenswall.com/";





$obj_db = new db();



$obj_db->open_connection();



?>