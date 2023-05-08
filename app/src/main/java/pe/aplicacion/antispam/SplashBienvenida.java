package pe.aplicacion.antispam;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import java.util.Timer;
import java.util.TimerTask;

public class SplashBienvenida extends AppCompatActivity {

    TextView txtLogo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash_bienvenida);
        txtLogo =findViewById(R.id.txtLogoSplash);

        new Timer().schedule(new TimerTask() {
            @Override
            public void run() {
                llamar_Main(txtLogo);
            }

            private void llamar_Main(View view) {
                Intent i = new Intent(SplashBienvenida.this, Comenzar.class);
                startActivity(i);
            }
        },3000);




    }
}