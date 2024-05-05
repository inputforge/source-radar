export default function Avatar({value}: { value: string }) {

    const hash = value.split("").reduce((acc: number, char: string) => {
        acc = ((acc << 5) - acc) + char.charCodeAt(0)
        return acc & acc
    }, 0)

    const hue = Math.abs(hash % 360)
    const saturation = 50
    const lightness = 50


    const bits = (hash & 0xFFFF).toString(2).padStart(16, "0").split("").map(bit => bit === "1")


    return (
        <svg preserveAspectRatio="true" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
            {bits.map((bit, index) => (
                <rect
                    key={index}
                    x={index % 4 * 4}
                    y={Math.floor(index / 4) * 4}
                    width={4}
                    height={4}
                    fill={bit ? `hsl(${hue}, ${saturation}%, ${lightness}%)` : "#fff"}
                />
            ))}
        </svg>
    )

}