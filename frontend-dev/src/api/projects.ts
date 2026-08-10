/*Purpose: Communicate with backend FASTApit*/
import type {Project} from "../type/projects"; 

/*Asynchronous: computer process that runs into the background without making the main program wait */
export async function getProjects(): Promise <Project[] >{

    /*Wait until sucessfullt retrieved*/
    const response = await fetch("http://127.0.0.1:8000/api/projects");

    /*Parse Response to JSON*/ 
    if(!response.ok) {
        throw new Error("FAILED: Unable to fetch the projects")
    }

    /*Convert RAW response to usable  JSON data */
    const projects : Project []  = await response.json(); 


    return projects; 

}

    
