"use client";

import React, { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Layout from "@/app/components/Layout";

interface Article {
    id: number;
    title: string;
    content: string;
};

export default function ArticlePage() {
    const { id } = useParams();
    const [article, setArticle] = useState<Article | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        if (id) {
            fetch(`http://localhost:5000/articles/${id}`)
                .then((response) => {
                    if (!response.ok) {
                        throw new Error("Error al obtener el artículo");
                    }
                    return response.json();
                })
                .then((data) => {
                    setArticle(data);
                    setLoading(false);
                })
                .catch((error) => {
                    console.log("Error al obtener el articulo:", error);
                    setError(error.message);
                    setLoading(false);
                });
        }
    }, [id]);

    return (
        <Layout>
            <div className="container mx-auto py-10">
                {loading ? (
                    <p className="text-gray-600">Cargando artículo...</p>
                ) : error ? (
                    <p className="text-red-600">Error: {error}</p>
                ) : article ? (
                    <article className="bg-white rounded-lg shadow-md p-6">
                        <h1 className="text-4xl font-bold mb-4 text-indigo-600">{article.title}</h1>
                        <div className="text-gray-700 whitespace-pre-wrap">{article.content}</div>
                        <a href="/" className="text-indigo-600 hover:text-indigo-800 font-medium mt-6 inline-block">
                            ← Volver a los artículos
                        </a>
                    </article>
                ) : (
                    <p className="text-gray-600">Artículo no encontrado.</p>
                )}
            </div>
        </Layout>
    );
}


