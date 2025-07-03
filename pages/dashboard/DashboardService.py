from app_enums.http_methods_enum import HttpMethodsEnum
from app_service.requestService import RequestService
from config.app_config import config
from helpers.showMessages import ShowMessages

class DashboardService(ShowMessages):
    requestService = RequestService()
    powerStateId = "6861eaa04f7164f10fb6d1e6"

    def toggle_machine_power_state(self, state:str):
        self.requestService.makeRequest(
            HttpMethodsEnum.put,
            self.on_failure_toggle_machine_state,
            self.on_success_toggle_machine_state,
            config.get("URL_BASE") + "/machine-state/" + self.powerStateId,
            None,
            { "power": state }
        )

    def on_success_toggle_machine_state(self, req, res):
        self.showToast("Cambio el estado con exito")

    def on_failure_toggle_machine_state(self, req, res):
        print(res)
        self.showToast("Ocurrio un error al intentar cambiar el estado de la maquina")

    def load_machine_power_state(self):
        self.requestService.makeRequest(
            method=HttpMethodsEnum.get,
            on_failure= lambda x: None,
            on_success=lambda x: None,
            url=config.get("URL_BASE") + "machine-state"
        )

    def on_success_load_machine_power_state(self, req, result):
        if len(result) == 1:
            for item in result:
                print(item)
                self.powerStateId = item._id

    def on_failure_load_machine_power_state(self, req, result):
        self.showToast("Ocurrio un error insperado al intentar sincronizar el estado.")

