import { useState } from "react"
import axios from 'axios';

export default function AddItem() {
    const [list, setList] = useState([])
    const [value, setValue] = useState('')

    function handleChange(evt) {
        setValue(evt.target.value)
    }
    function handleAdd() {
        const response = axios.post('http://localhost:8000/add', { value: value }, {
            headers: {
                'Content-Type': 'application/json',
            }
        })
        setList([...list, value])
        setValue('')
    }
    function handleDelete(i) {
        const response = axios.post(`http://localhost:8000/delete`, { value: list[i] }, {
            headers: {
                'Content-Type': 'application/json',
            }
        })
        setList(list.filter((_, index) => index !== i))
    }

    return (
        <div>
            <input type="text" value={value} onChange={handleChange} />
            <button onClick={handleAdd}>Add Item</button>
            <div>
                <ul>
                    {list.map((item, index) => (
                        <div><li key={index}>{item}</li> <button onClick={() => handleDelete(index)}>Delete</button></div>
                    ))}
                </ul>
            </div>
        </div>

    )
}