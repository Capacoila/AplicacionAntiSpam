package pe.aplicacion.antispam;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Comenzar extends AppCompatActivity {
    Button btnComenzar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_comenzar);
        btnComenzar=findViewById(R.id.buttonComenzar);
        btnComenzar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                BlockPrede();
            }

            private void BlockPrede() {
                Intent i = new Intent(Comenzar.this, BlockPredeterminada.class);
                startActivity(i);
            }
        });
    }
}