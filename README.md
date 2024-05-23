        data class PythonAnswer (
            val address: Portes
        )
        
        data class Portes(
            val ports: List<Port>
        )
        
        data class Port(
            val portid: String,
            val protocol: String,
            val reason: String,
            val reason_ttl: String,
            val scripts: List<Script>,
            val service: Service,
            val state: String,
        )
        
        open class Script(
            val data: Map<String, Cpe>? = emptyMap()
        )
        
        data class Cpe(
            val children: List<Children>,
        )
        
        data class Children(
            val cvss: String,
            val id: String,
            val is_exploit: String? = "false",
            val type: String,
        )
        
        data class Service(
            val conf: String,
            val extrainfo: String? = null,
            val method: String,
            val name: String,
            val ostype: String? = null,
            val product: String? = null,
            val version: String? = null,
        )
