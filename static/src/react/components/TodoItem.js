/* @odoo-module */

// import React, { useState } from 'react';
// import { FaTrash } from 'react-icons/fa';
// import styles from './TodoItem.module.css';

const TodoItem = (props) => {
  const [editing, setEditing] = useState(false);

  const handleEditing = () => {
    setEditing(true);
  };

  const handleUpdatedDone = (event) => {
    if (event.key === 'Enter') {
      setEditing(false);
    }
  };

  const completedStyle = {
    fontStyle: 'italic',
    color: '#595959',
    opacity: 0.4,
    textDecoration: 'line-through',
  };

  const {
    todo, deleteTodoProps, handleChangeProps, setUpdate,
  } = props;

  const viewMode = {};
  const editMode = {};

  if (editing) {
    viewMode.display = 'none';
  } else {
    editMode.display = 'none';
  }

  return (
    <li className={"item"}>
      <div onDoubleClick={handleEditing} style={viewMode}>
        <input
          type="checkbox"
          className={"checkbox"}
          checked={todo.completed}
          onChange={() => handleChangeProps(todo.id)}
        />
        <button type="submit" onClick={() => deleteTodoProps(todo.id)}>
          Del
        </button>
        <span style={todo.completed ? completedStyle : null}>{todo.title}</span>
      </div>
      <input
        type="text"
        style={editMode}
        className={"textInput"}
        value={todo.title}
        onChange={(e) => {
          setUpdate(e.target.value, todo.id);
        }}
        onKeyDown={handleUpdatedDone}
      />
    </li>
  );
};

export default TodoItem;
