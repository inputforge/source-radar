import {NavLink} from "react-router-dom";
import {Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle} from "@/components/ui/card.tsx";
import {Input} from "@/components/ui/input.tsx";
import {Button} from "@/components/ui/button.tsx";
import {Checkbox} from "@/components/ui/checkbox.tsx";

export default function Settings() {
    return (
        <>
            <div className="mx-auto grid w-full max-w-6xl gap-2">
                <h1 className="text-3xl font-semibold">Settings</h1>
            </div>
            <div
                className="mx-auto grid w-full max-w-6xl items-start gap-6 md:grid-cols-[180px_1fr] lg:grid-cols-[250px_1fr]">
                <nav
                    className="grid gap-4 text-sm text-muted-foreground"
                >
                    <NavLink to="/settings" className="font-semibold text-primary">
                        General
                    </NavLink>
                    <NavLink to="/settings/">Integrations</NavLink>
                    <NavLink to="/settings/">Advanced</NavLink>
                </nav>
                <div className="grid gap-6">
                    <Card>
                        <CardHeader>
                            <CardTitle>Organization</CardTitle>
                            <CardDescription>
                                Update your organization's name and other details.
                            </CardDescription>
                        </CardHeader>
                        <CardContent>
                            <form>
                                <Input placeholder="Organization name" />
                            </form>
                        </CardContent>
                        <CardFooter className="border-t px-6 py-4">
                            <Button>Save</Button>
                        </CardFooter>
                    </Card>
                </div>
            </div>
        </>
    )
}