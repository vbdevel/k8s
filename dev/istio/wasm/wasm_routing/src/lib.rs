extern crate wasm_bindgen;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn route_request(header_value: &str) -> String {
    match header_value {
        "24.3.0.1" => "http://first-svc-cluster.default.svc.cluster.local",
        "24.4.0.1" => "http://second-svc-cluster.default.svc.cluster.local",
        _ => "http://first-svc-cluster.default.svc.cluster.local",
    }.to_string()
}

