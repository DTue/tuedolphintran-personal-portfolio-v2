import type {Project} from "../type/projects"


/*Project Card*/
type ProjectCardElement = {
    project: Project; 
}
function ProjectCard({project} : ProjectCardElement){
    return(
        <section className = "project-card-component">
           {/*<img className="project-img" src ={project.image_url}> </img> */}
            <p className="project-category">{project.category}</p>
            <h3>{project.title}</h3>
            <p className="project-role">{project.role}</p>
            <p className="project-summary">{project.summary}</p>
            <p className="github-url">{project.github_url}</p>
            <p className="demo-url">{project.demo_url}</p>
            <p className="featured">{project.featured}</p>
        </section>
    );
}
export default ProjectCard; 
