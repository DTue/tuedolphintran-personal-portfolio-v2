import { useEffect, useState } from "react";
import { getProjects } from "../api/projects";
import ProjectCard from "../components/ProjectCard"; 
import type { Project } from "../type/projects"; 

function ProjectsTest() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getProjects()
      .then((data) => setProjects(data))
      .catch((err) => {
        console.error(err);
        setError("Could not load projects.");
      });
  }, []);

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <section>
      <h2>Projects API Test</h2>

      {projects.map((project) => (
        <ProjectCard
          key={project.id}
          project={project}
        />
      ))}
    </section>
  );
}export default ProjectsTest;