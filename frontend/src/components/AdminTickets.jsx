import { useEffect, useState } from "react";

import { getTickets } from "../services/api.js";

function formatDate(value) {
  if (!value) return "-";
  return new Intl.DateTimeFormat("tr-TR", {
    dateStyle: "short",
    timeStyle: "short",
  }).format(new Date(value));
}

function truncate(text, maxLength = 96) {
  if (text.length <= maxLength) return text;
  return `${text.slice(0, maxLength)}...`;
}

function AdminTickets() {
  const [tickets, setTickets] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  async function loadTickets() {
    setIsLoading(true);
    setError("");
    try {
      const data = await getTickets();
      setTickets(data);
    } catch (loadError) {
      setError(loadError.message);
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    loadTickets();
  }, []);

  const total = tickets.length;
  const highPriority = tickets.filter((ticket) => ticket.priority_level === "Yüksek").length;
  const newTickets = tickets.filter((ticket) => ticket.status === "Yeni").length;

  return (
    <section className="admin-page">
      <div className="admin-header">
        <div>
          <p className="eyebrow">Admin Paneli</p>
          <h1>Gelen talepler</h1>
          <p>AI tarafından kategori, birim ve temel öncelik bilgisi eklenen kayıtlar.</p>
        </div>
        <button className="secondary-button" type="button" onClick={loadTickets} disabled={isLoading}>
          {isLoading ? "Yenileniyor..." : "Listeyi Yenile"}
        </button>
      </div>

      <div className="stats-grid">
        <article className="stat-card">
          <span>Toplam Talep</span>
          <strong>{total}</strong>
        </article>
        <article className="stat-card">
          <span>Yeni Durumda</span>
          <strong>{newTickets}</strong>
        </article>
        <article className="stat-card urgent">
          <span>Yüksek Öncelik</span>
          <strong>{highPriority}</strong>
        </article>
      </div>

      <div className="panel table-panel">
        {error && <div className="alert error">{error}</div>}

        {isLoading && <div className="empty-state">Talepler yükleniyor...</div>}

        {!isLoading && !error && tickets.length === 0 && (
          <div className="empty-state">
            Henüz talep yok. Demo için önce <a href="/report">talep formundan</a> kayıt oluştur.
          </div>
        )}

        {!isLoading && tickets.length > 0 && (
          <div className="table-scroll">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Açıklama</th>
                  <th>Kategori</th>
                  <th>Birim</th>
                  <th>Konum</th>
                  <th>Öncelik</th>
                  <th>Durum</th>
                  <th>Tarih</th>
                </tr>
              </thead>
              <tbody>
                {tickets.map((ticket) => (
                  <tr key={ticket.id}>
                    <td>#{ticket.id}</td>
                    <td>
                      <strong>{truncate(ticket.description)}</strong>
                      {ticket.ai_reason && <small>{truncate(ticket.ai_reason, 120)}</small>}
                    </td>
                    <td><span className="pill blue">{ticket.category}</span></td>
                    <td>{ticket.department}</td>
                    <td>{ticket.district} / {ticket.neighborhood}</td>
                    <td><span className={`pill priority-${ticket.priority_level.toLowerCase()}`}>{ticket.priority_level}</span></td>
                    <td><span className="pill">{ticket.status}</span></td>
                    <td>{formatDate(ticket.created_at)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </section>
  );
}

export default AdminTickets;
