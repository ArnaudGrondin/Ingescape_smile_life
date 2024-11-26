package com.example.smile_life

import android.graphics.Color
import android.net.nsd.NsdManager
import android.net.nsd.NsdServiceInfo
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.core.content.ContextCompat.getSystemService
import com.example.smile_life.ui.theme.Pink80
import com.example.smile_life.ui.theme.Purple80
import com.example.smile_life.ui.theme.PurpleGrey80
import com.example.smile_life.ui.theme.Smile_LifeTheme
import java.net.ServerSocket


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Smile_LifeTheme {
                connectGame(modifier = Modifier.fillMaxSize())

            }
        }
    }
}


fun registerService(port: Int,joueur: String) {
    // Create the NsdServiceInfo object, and populate it.
    val serviceInfo = NsdServiceInfo().apply {
        // The name is subject to change based on conflicts
        // with other services advertised on the same network.
        serviceName = "NsdChat + String"
        serviceType = "_nsdchat._tcp"
        setPort(port)
    }
}

fun initializeServerSocket() {
    // Initialize a server socket on the next available port.
    var serverSocket = ServerSocket(0).also { socket ->
        // Store the chosen port.
        var mLocalPort = socket.localPort

    }
}

private val registrationListener = object : NsdManager.RegistrationListener {

    override fun onServiceRegistered(NsdServiceInfo: NsdServiceInfo) {
        // Save the service name. Android may have changed it in order to
        // resolve a conflict, so update the name you initially requested
        // with the name Android actually used.
        var mServiceName = NsdServiceInfo.serviceName
    }

    override fun onRegistrationFailed(serviceInfo: NsdServiceInfo, errorCode: Int) {
        // Registration failed! Put debugging code here to determine why.
    }

    override fun onServiceUnregistered(arg0: NsdServiceInfo) {
        // Service has been unregistered. This only happens when you call
        // NsdManager.unregisterService() and pass in this listener.
    }

    override fun onUnregistrationFailed(serviceInfo: NsdServiceInfo, errorCode: Int) {
        // Unregistration failed. Put debugging code here to determine why.
    }
}
fun registerService(port: Int) {
    // Create the NsdServiceInfo object, and populate it.
    val serviceInfo = NsdServiceInfo().apply {
        // The name is subject to change based on conflicts
        // with other services advertised on the same network.
        serviceName = "NsdChat"
        serviceType = "_nsdchat._tcp"
        setPort(port)
    }

   // nsdManager = (getSystemService(Context.NSD_SERVICE) as NsdManager).apply {
   //     registerService(serviceInfo, NsdManager.PROTOCOL_DNS_SD, registrationListener)
   // }
}


@Composable
fun connectGame(modifier: Modifier = Modifier){

    Column(modifier = modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally,
            ) {
        Text(" Smile Life ",color = Pink80, fontSize = 30.sp)
        recevoirNom()
        Button(onClick = {/* */},modifier.padding(12.dp)) {
            Text("Se connecter")
        }

    }

}

@Composable
fun recevoirNom(){
    var text by remember { mutableStateOf(" ")}

    TextField(
            value = text,
            onValueChange = {text = it},
            label = { Text("NomJoueur") }
        )
}
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    Smile_LifeTheme {
        connectGame()
    }
}