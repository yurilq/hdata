provider "google" {
  project = "hdata-projeto"
  region  = "us-central1"
}

resource "google_storage_bucket" "hdata_bucket" {
  name     = "hdata-bucket"
  location = "US"
}

resource "google_bigquery_dataset" "hdata_dataset" {
  dataset_id = "hdata_financeiro"
  location   = "US"
}

resource "google_bigquery_table" "hdata_table" {
  dataset_id = google_bigquery_dataset.hdata_dataset.dataset_id
  table_id   = "dados_enriquecidos"
  schema     = file("schemas/tabela_enriquecida_hdata_schema.json")
}
