import AdminTickets from "./components/AdminTickets.jsx";
import ReportForm from "./components/ReportForm.jsx";

function App() {
  const path = window.location.pathname;
  const isAdmin = path.startsWith("/admin/tickets");

  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href="/report" aria-label="ŞehirPulse AI ana sayfa">
          <span className="brand-mark">SP</span>
          <span>
            <strong>ŞehirPulse AI</strong>
            <small>Belediye Talep Yönetimi</small>
          </span>
        </a>
        <nav className="nav-links" aria-label="Ana navigasyon">
          <a className={!isAdmin ? "active" : ""} href="/report">Talep Gönder</a>
          <a className={isAdmin ? "active" : ""} href="/admin/tickets">Admin Paneli</a>
        </nav>
      </header>

      <main>{isAdmin ? <AdminTickets /> : <ReportForm />}</main>
    </div>
  );
}

export default App;
