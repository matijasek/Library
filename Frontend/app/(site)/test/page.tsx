"use client"

import { useEffect } from "react";

export default function() {
  useEffect(() => {
    (async () => {
      // http://frontend:3000
      const res = await fetch("http://localhost:8081/waz/books/");
      const data = await res.json();
      console.log(data);
    })()
  }, [])


  return <p>Test page</p>;
}