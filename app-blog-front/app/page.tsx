"use client";

import Layout from "@/app/components/Layout";
import { useEffect, useState } from "react";

type Article = {
  id: number;
  title: string;
  content: string;
};

export default function Home() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://localhost:5000/articles")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Error al obtener los artículos");
        }
        return response.json();
      })
      .then((data) => {
        setArticles(data);
        setLoading(false);
      })
      .catch((error) => {
        console.log("Error al obtener los articulos:", error);
        setError(error.message);
        setLoading(false);
      });

  }, []);

  return (
    <>
      <Layout>
          <div className="container mx-auto py-10">
            <h1 className="text-4xl font-bold mb-6 text-indigo-600">Últimos artículos</h1>
            
            {loading ? (
              <p className="text-gray-600">Cargando artículos...</p>
            ) : error ? (
              <p className="text-red-600">Error: {error}</p>
            ) : articles.length === 0 ? (
              <p className="text-gray-600">No hay artículos disponibles.</p>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {articles.map((article) => (
                  <div key={article.id} className="bg-white rounded-lg shadow-md p-6">
                    <h2 className="text-2xl font-semibold mb-4 text-gray-800">{article.title}</h2>
                    <p className="text-gray-600 mb-4">{article.content.slice(0, 100)}...</p>
                    <link href={`/article/${article.id}`} className="text-indigo-600 hover:text-indigo-800 font-medium">
                      Leer más →
                    </link>
                  </div>
                ))}
              </div>
            )}
          </div>
      </Layout>
    </>
  );
}
