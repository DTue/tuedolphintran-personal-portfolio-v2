export type Project = {
    id: number;
    title: string;
    slug: string;
    category: string;
    role: string;
    summary: string;
    image_url: string;
    github_url: string;
    demo_url: string;
    featured: boolean;
    display_order: number;
};