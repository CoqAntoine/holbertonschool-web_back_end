export default function hasValuesFromArray(a, array) {
    return array.every(element => a.has(element))
}
