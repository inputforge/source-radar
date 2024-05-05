const cache: Record<string, any> = {};


export function query(key: string, fn: () => Promise<any>) {
    if (!cache[key]) {
        cache[key] = fn();
    }
    return cache[key];
}

export function invalidate(...key: (string | RegExp)[]) {
    key.forEach(k => {
        if (typeof k === "string") {
            delete cache[k];
        } else {
            Object.keys(cache).forEach(key => {
                if (k.test(key)) {
                    delete cache[key];
                }
            });
        }
    });
}

export function api(method: string, url: string, body?: any) {
    return fetch(`/api/v1${url}`, {
        method,
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
    }).then(res => res.json());
}
