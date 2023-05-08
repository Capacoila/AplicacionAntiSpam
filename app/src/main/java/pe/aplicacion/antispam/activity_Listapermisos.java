package pe.aplicacion.antispam;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class activity_Listapermisos extends AppCompatActivity implements View.OnClickListener {
    TextView txtCancel,txtContinue;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_listapermisos);
        txtCancel = findViewById(R.id.textview_Cancelar);
        txtContinue = findViewById(R.id.textview_Continuar);
    }

    @Override
    public void onClick(View view) {

    }
}