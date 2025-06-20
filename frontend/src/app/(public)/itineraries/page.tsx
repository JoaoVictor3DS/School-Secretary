"use client";

import axios from "axios";

import Link from "next/link";
import React, { useState, useEffect } from "react";

import SearchField from "@/components/SearchField";

import { ItineraryProps } from "@/types/itinerary";
import { ITINERARY_BASE_URL } from "@/config";

export default function ItinerariesPage() {
	const [search, setSearch] = useState("");
	const [data, setData] = useState<ItineraryProps[]>([]);

	useEffect(() => {
		axios
			.get<ItineraryProps[]>(`${ITINERARY_BASE_URL}?search=${search}`)
			.then((response) => setData(response.data))
			.catch((error) => {
				alert(`Erro ao carregar itinerários: ${error}`);
			});
	}, [search]);

	const handleSearch = (value: string) => {
		setSearch(value);
	};

	const handleDelete = (value: number) => {
		axios.delete(`${ITINERARY_BASE_URL}${value}/`);
	};

	return (
		<div>
			<div className="flex justify-center">
				<div className="title-container">
					<h1 className="title">Itinerários</h1>
				</div>
			</div>

			<div className="flex flex-row items-center justify-center">
				<SearchField
					placeholder="Buscar itinerário..."
					onSearch={handleSearch}
				/>
			</div>
			<div className="flex justify-center m-3">
				<Link
					className="link link-common w-50 text-center"
					href="/itineraries/add"
				>
					Adicionar
				</Link>
			</div>
			<div>
				<div className="flex justify-center items-center">
					<div className="table-container">
						<table className="m-3 table table-border">
							<thead>
								<tr>
									<th>Abreviação</th>
									<th>Nome completo</th>
									<th>Remover</th>
								</tr>
							</thead>
							<tbody>
								{data.map((itinerary) => (
									<tr key={itinerary.id}>
										<td>{itinerary.short_name}</td>
										<td>{itinerary.full_name}</td>
										<td>
											<button
												className="link link-blue"
												onClick={() =>
													handleDelete(itinerary.id)
												}
											>
												Remover
											</button>
										</td>
									</tr>
								))}
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
	);
}
