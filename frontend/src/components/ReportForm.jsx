import { useState } from "react";

import { createTicket } from "../services/api.js";

const initialForm = {
  citizen_name: "",
  description: "",
  district: "",
  neighborhood: "",
  address: "",
  request_type: "Şikayet",
};

const districts = ["Kadıköy", "Üsküdar", "Beşiktaş", "Bakırköy", "Ataşehir", "Maltepe", "Pendik", "Diğer"];

function validate(form) {
  const errors = {};

  if (form.description.trim().length < 10) {
    errors.description = "Talep açıklaması en az 10 karakter olmalı.";
  }
  if (!form.district) {
    errors.district = "İlçe seçilmelidir.";
  }
  if (!form.neighborhood.trim()) {
    errors.neighborhood = "Mahalle bilgisi zorunludur.";
  }
  if (!form.request_type) {
    errors.request_type = "Talep türü seçilmelidir.";
  }

  return errors;
}

function ReportForm() {
  const [form, setForm] = useState(initialForm);
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState("");
  const [createdTicket, setCreatedTicket] = useState(null);

  function updateField(event) {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
    setErrors((current) => ({ ...current, [name]: undefined }));
  }

  async function handleSubmit(event) {
    event.preventDefault();
    const validationErrors = validate(form);
    setErrors(validationErrors);
    setSubmitError("");
    setCreatedTicket(null);

    if (Object.keys(validationErrors).length > 0) {
      return;
    }

    setIsSubmitting(true);
    try {
      const ticket = await createTicket({
        ...form,
        citizen_name: form.citizen_name.trim() || "Anonim",
        description: form.description.trim(),
        neighborhood: form.neighborhood.trim(),
        address: form.address.trim() || null,
      });
      setCreatedTicket(ticket);
      setForm(initialForm);
    } catch (error) {
      setSubmitError(error.message);
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <section className="page-grid report-page">
      <div className="hero-card">
        <p className="eyebrow">Vatandaş Bildirim Ekranı</p>
        <h1>Mahallendeki problemi belediyeye hızlıca ilet.</h1>
        <p>
          ŞehirPulse AI talebini kaydeder, açıklama metnini analiz eder ve ilgili belediye birimine yönlendirir.
        </p>
        <div className="flow-strip" aria-label="Talep akışı">
          <span>Form</span>
          <span>AI Kategori</span>
          <span>Birim</span>
          <span>Admin Liste</span>
        </div>
      </div>

      <form className="panel form-card" onSubmit={handleSubmit} noValidate>
        <div className="section-heading">
          <p className="eyebrow">Yeni Talep</p>
          <h2>Talep bilgileri</h2>
        </div>

        <label>
          Ad soyad <span>opsiyonel</span>
          <input
            name="citizen_name"
            value={form.citizen_name}
            onChange={updateField}
            placeholder="Boş bırakılırsa Anonim gönderilir"
          />
        </label>

        <label>
          Talep açıklaması
          <textarea
            name="description"
            value={form.description}
            onChange={updateField}
            placeholder="Örn. Mahallemizdeki sokak lambası 3 gündür yanmıyor."
            rows="6"
          />
          {errors.description && <small className="field-error">{errors.description}</small>}
        </label>

        <div className="form-row">
          <label>
            İlçe
            <select name="district" value={form.district} onChange={updateField}>
              <option value="">Seçiniz</option>
              {districts.map((district) => (
                <option key={district} value={district}>{district}</option>
              ))}
            </select>
            {errors.district && <small className="field-error">{errors.district}</small>}
          </label>

          <label>
            Mahalle
            <input name="neighborhood" value={form.neighborhood} onChange={updateField} placeholder="Caferağa" />
            {errors.neighborhood && <small className="field-error">{errors.neighborhood}</small>}
          </label>
        </div>

        <label>
          Adres açıklaması <span>opsiyonel</span>
          <input name="address" value={form.address} onChange={updateField} placeholder="Moda Caddesi 12. Sokak" />
        </label>

        <fieldset>
          <legend>Talep türü</legend>
          {['Talep', 'Şikayet', 'İhbar'].map((type) => (
            <label className="radio-card" key={type}>
              <input
                type="radio"
                name="request_type"
                value={type}
                checked={form.request_type === type}
                onChange={updateField}
              />
              {type}
            </label>
          ))}
          {errors.request_type && <small className="field-error">{errors.request_type}</small>}
        </fieldset>

        {submitError && <div className="alert error">{submitError}</div>}

        {createdTicket && (
          <div className="alert success">
            <strong>Talebiniz alınmıştır. Talep No: #{createdTicket.id}</strong>
            <span>{createdTicket.category} → {createdTicket.department}</span>
          </div>
        )}

        <button className="primary-button" type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Gönderiliyor..." : "Talebi Gönder"}
        </button>
      </form>
    </section>
  );
}

export default ReportForm;
