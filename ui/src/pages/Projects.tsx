// import Image from "next/image"
import {MoreHorizontal, PlusCircle} from "lucide-react"

import {Badge} from "@/components/ui/badge"
import {Button} from "@/components/ui/button"
import {Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle,} from "@/components/ui/card"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {Table, TableBody, TableCell, TableHead, TableHeader, TableRow,} from "@/components/ui/table"
import Avatar from "@/pages/Avatar.tsx";
import {Link, useLoaderData} from "react-router-dom";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger
} from "@/components/ui/dialog.tsx";

import {Label} from "@/components/ui/label";
import {Input} from "@/components/ui/input.tsx";

interface Project {
    id: number
    name: string
}

export default function Projects() {

    const projects = useLoaderData() as Project[]

    return (
        <>
            <div className="flex items-center">
                <div className="ml-auto flex items-center gap-2">
                    <Dialog>
                        <DialogTrigger asChild>
                            <Button size="sm" className="h-8 gap-1">
                                <PlusCircle className="h-3.5 w-3.5"/>
                                <span className="sr-only sm:not-sr-only sm:whitespace-nowrap">Add Project</span>
                            </Button>
                        </DialogTrigger>
                        <DialogContent className="sm:max-w-[425px]">
                            <DialogHeader>
                                <DialogTitle>Add project</DialogTitle>
                                <DialogDescription>
                                    Add a new project to your account.
                                </DialogDescription>
                            </DialogHeader>
                            <div className="grid gap-4 py-4">
                                <div className="grid grid-cols-4 items-center gap-4">
                                    <Label htmlFor="name" className="text-right">
                                        Name
                                    </Label>
                                    <Input
                                        id="name"
                                        defaultValue="Untitled Project"
                                        className="col-span-3"
                                    />
                                </div>
                            </div>
                            <DialogFooter>
                                <Button type="submit">Add</Button>
                            </DialogFooter>
                        </DialogContent>
                    </Dialog>

                </div>
            </div>
            <Card>
                <CardHeader>
                    <CardTitle>Projects</CardTitle>
                    <CardDescription>
                        Manage your projects
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <Table>
                        <TableHeader>
                            <TableRow>
                                <TableHead className="hidden w-[100px] sm:table-cell">
                                    <span className="sr-only">Image</span>
                                </TableHead>
                                <TableHead>Name</TableHead>
                                <TableHead>Status</TableHead>
                                <TableHead className="hidden md:table-cell">
                                    Open Issues
                                </TableHead>
                                {/*<TableHead className="hidden md:table-cell">Last scan</TableHead>*/}
                                <TableHead>
                                    <span className="sr-only">Actions</span>
                                </TableHead>
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            {projects.map((project) => (
                                <TableRow key={project.id}>
                                    <TableCell className="hidden sm:table-cell">
                                        <Link to={`/projects/${project.id}`}>
                                            <Avatar value={project.name}/>
                                        </Link>
                                    </TableCell>
                                    <TableCell className="font-medium">
                                        <Link to={`/projects/${project.id}`}>
                                            {project.name}
                                        </Link>
                                    </TableCell>
                                    <TableCell>
                                        <Badge variant="outline">Passed</Badge>
                                    </TableCell>
                                    <TableCell className="hidden md:table-cell">0</TableCell>
                                    <TableCell>
                                        <DropdownMenu>
                                            <DropdownMenuTrigger asChild>
                                                <Button aria-haspopup="true" size="icon" variant="ghost">
                                                    <MoreHorizontal className="h-4 w-4"/>
                                                    <span className="sr-only">Toggle menu</span>
                                                </Button>
                                            </DropdownMenuTrigger>
                                            <DropdownMenuContent align="end">
                                                <DropdownMenuLabel>Actions</DropdownMenuLabel>
                                                <DropdownMenuItem>Edit</DropdownMenuItem>
                                                <DropdownMenuItem>Delete</DropdownMenuItem>
                                            </DropdownMenuContent>
                                        </DropdownMenu>
                                    </TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </CardContent>
                <CardFooter>
                    {/*<div className="text-xs text-muted-foreground">*/}
                    {/*    Showing <strong>1-10</strong> of <strong>32</strong> products*/}
                    {/*</div>*/}
                </CardFooter>
            </Card>
        </>
    )
}
